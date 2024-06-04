(define (for start end fn i)
        (if (> start end)
        0
        (+ (fn i) (for (start + 1) end fn i))))

