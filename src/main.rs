#![no_std]
#![no_main]

mod euclidean;

use embassy_executor::Spawner;
// use embassy_futures::select::{Either, select};
use embassy_rp::gpio::{Input, Level, Output, Pull};
use embassy_sync::blocking_mutex::raw::CriticalSectionRawMutex;
use embassy_sync::signal::Signal;
use embassy_time::Timer;
use euclidean::euclidean_rhythm;
use panic_halt as _;

const PATTERN: [u8; 8] = euclidean_rhythm::<8>(3, 8);
const TRIGGER_LENGTH_MS: u64 = 100;

static TRIGGER_SIGNAL: Signal<CriticalSectionRawMutex, ()> = Signal::new();

#[embassy_executor::task]
async fn trigger_task(mut clock_in: Input<'static>) {
    loop {
        clock_in.wait_for_rising_edge().await;
        TRIGGER_SIGNAL.signal(());
        clock_in.wait_for_falling_edge().await;
    }
}

#[embassy_executor::main]
async fn main(spawner: Spawner) {
    let p = embassy_rp::init(Default::default());
    let mut led = Output::new(p.PIN_15, Level::Low);
    let clock = Input::new(p.PIN_14, Pull::Down);

    // Is there a way to handle the potential error cases resulting from the
    // spawn? I will ignore this for now, and get back to it later.
    spawner.spawn(trigger_task(clock)).unwrap();

    let mut playhead = 0;

    loop {
        TRIGGER_SIGNAL.wait().await;
        TRIGGER_SIGNAL.reset();

        if PATTERN[playhead] == 1 {
            led.set_high();
            Timer::after_millis(TRIGGER_LENGTH_MS).await;
            led.set_low();
        }

        playhead += 1;
        if playhead >= PATTERN.len() {
            playhead = 0;
        }
    }
}
