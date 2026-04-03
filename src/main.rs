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

// const BEAT_OFF_MS: u64 = 200;
// const REST_MS: u64 = 300;

static TRIGGER_SIGNAL: Signal<CriticalSectionRawMutex, ()> = Signal::new();

#[embassy_executor::task]
async fn trigger_task(mut button: Input<'static>) {
    loop {
        button.wait_for_rising_edge().await;
        TRIGGER_SIGNAL.signal(());
    }
}

// async fn wait_or_signal(ms: u64) -> bool {
//     match select(Timer::after_millis(ms), TRIGGER_SIGNAL.wait()).await {
//         Either::First(_) => false,
//         Either::Second(_) => true,
//     }
// }

#[embassy_executor::main]
async fn main(spawner: Spawner) {
    let p = embassy_rp::init(Default::default());
    let mut led = Output::new(p.PIN_15, Level::Low);
    let trigger = Input::new(p.PIN_14, Pull::Down);

    // Is there a way to handle the potential error cases resulting from the
    // spawn? I will ignore this for now, and get back to it later.
    spawner.spawn(trigger_task(trigger)).unwrap();

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

    // This is the old logic where the trigger signal is used for play/stop
    /*
    loop {
        TRIGGER_SIGNAL.wait().await;
        TRIGGER_SIGNAL.reset();

        'playing: for step in (0..PATTERN.len()).cycle() {
            if PATTERN[step] == 1 {
                led.set_high();
                if wait_or_signal(BEAT_ON_MS).await {
                    led.set_low();
                    break 'playing;
                }
                led.set_low();
                if wait_or_signal(BEAT_OFF_MS).await {
                    break 'playing;
                }
            } else if wait_or_signal(REST_MS).await {
                break 'playing;
            }
        }
    }
    */
}
