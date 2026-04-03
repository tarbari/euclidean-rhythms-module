pub const fn euclidean_rhythm<const N: usize>(k: usize, n: usize) -> [u8; N] {
    assert!(n <= N, "n must not exceed array capacity N");
    assert!(k <= n, "k (beats) must not exceed n (steps)");

    let mut result = [0u8; N];

    if k == 0 || n == 0 {
        return result;
    }
    if k >= n {
        let mut i = 0;
        while i < n { result[i] = 1; i += 1; }
        return result;
    }

    let mut a = [0u8; N];
    let mut a_len = 1usize;
    let mut a_count = k;
    a[0] = 1;

    let mut b = [0u8; N];
    let mut b_len = 1usize;
    let mut b_count = n - k;

    let mut z: isize = b_count as isize;

    while z > 0 || (if a_count < b_count { a_count } else { b_count }) > 1 {
        let k_var = if a_count < b_count { a_count } else { b_count };
        z -= k_var as isize;

        let new_a_len = a_len + b_len;
        let mut new_a = [0u8; N];
        let mut i = 0;
        while i < a_len { new_a[i] = a[i]; i += 1; }
        let mut i = 0;
        while i < b_len { new_a[a_len + i] = b[i]; i += 1; }

        if a_count <= b_count {
            b_count -= a_count;
        } else {
            let old_a_count = a_count;
            a_count = b_count;
            b_count = old_a_count - b_count;
            let mut i = 0;
            while i < a_len { b[i] = a[i]; i += 1; }
            b_len = a_len;
        }

        let mut i = 0;
        while i < new_a_len { a[i] = new_a[i]; i += 1; }
        a_len = new_a_len;
    }

    let mut pos = 0;
    let mut rep = 0;
    while rep < a_count {
        let mut i = 0;
        while i < a_len { result[pos + i] = a[i]; i += 1; }
        pos += a_len;
        rep += 1;
    }
    let mut rep = 0;
    while rep < b_count {
        let mut i = 0;
        while i < b_len { result[pos + i] = b[i]; i += 1; }
        pos += b_len;
        rep += 1;
    }

    result
}
