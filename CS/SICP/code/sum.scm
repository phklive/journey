(define (cube x) (* x x x))

(define (inc x) (+ x 1))

(define (identity x) x)

(define (sum term a next b)
  (if (> a b)
  0
  (+ (term a)
  (sum term (next a) next b))))

(define (sum-iter term a next b)
  (define (iter a result)
    (if (> a b)
        result
        (iter (next a) (+ result (term a)))))
  (iter a 0))

(define (sum-integers a b)
  (sum identity a inc b))

(define (sum-integers-iter a b)
  (sum identity a inc b))

(define (sum-cubes a b)
  (sum cube a inc b))

(define (sum-cubes-iter a b)
  (sum cube a inc b))
