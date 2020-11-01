#lang sicp

(define (expmod base exp m)
  (cond ((= exp 0) 1)
        ((even? exp)
         (remainder (square (expmod base (/ exp 2) m))
                                    m))
        (else
         (remainder (* base (expmod base (- exp 1) m))
                         m)
       )))

(define (square x)
  (* x x))

(define (even? y)
  (= (remainder y 2) 0))

(define (fermat-test n)
  (define (try a)
    (= (expmod a n n) a))
  (try (+ 1 (random (- n 1)))))

(define (prime-test n times)
  (cond ((= times 0) true)
        ((fermat-test n) (prime-test n (- times 1)))
        (else false)))