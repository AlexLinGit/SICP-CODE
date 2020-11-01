#lang sicp

(define (fast-exp base n)
  (cond ((= n 0) 1)
        ((even? n) (square (fast-exp base (/ n 2))))
        (else (* base (fast-exp base (- n 1))))))

(define (square x)
  (* x x))

(define (even x)
  (= (remainder x 2) 0))

(define (expmod base exp m)
  (remainder (fast-exp base exp) m))