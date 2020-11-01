#lang sicp

;definitions
(define (square x)
  (* x x))

(define (even? y)
  (= (remainder y 2) 0))


;expmod
(define (expmod base exp m)
  (cond ((= exp 0) 1)
        ((even? exp)
         (remainder (square (expmod base (/ exp 2) m))
                                    m))
        (else
         (remainder (* base (expmod base (- exp 1) m))
                         m)
       )))

;fermat procedure
(define (fermat-test n counter)
  (define (try a)
     (= (expmod a n n) a))            
  (try counter))


;primality test
(define (prime-test-iter n counter)
  (cond ((= counter 0) true)
        ((fermat-test n counter) (prime-test-iter n (- counter
                                                       1)))
        (else false)))

(define (prime? n)
  (prime-test-iter n (- n 1)))
 