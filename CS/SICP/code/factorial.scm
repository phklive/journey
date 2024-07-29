(define (factorial-recursive n) (* n (factorial-recursive (- n 1))))

(define (factorial-iterative n)
  (define (iter product counter)
    (if (> counter n)
        product
        (iter (* counter product) (+ counter 1))))
(iter 1 1))
