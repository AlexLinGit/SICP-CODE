#lang sicp

(define (fast-mult a b)
  (mult-iter a b 0))

(define (mult-iter a b n)
  (cond ((= b 0) 0)
        ((= a 0) n)
        ((even a) (mult-iter (half a)
                             (double b)
                              n))
        (else (mult-iter (- a 1)
                         b
                         (+ n b)))
              ))

(define (double x)
  (+ x x))

(define (half x)
  (/ x 2))

(define (even x)
  (= (remainder x 2) 0))
