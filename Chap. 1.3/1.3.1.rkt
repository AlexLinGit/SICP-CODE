#lang sicp

(define (sum term a b next)
  (if (> a b)
      0
        (+ (term a)
           (sum term (next a) b next))))

(define (inc n)
  (+ n 1))

(define (cube n)
  (* n n n))

(define (sum-of-cubes a b)
  (sum cube a b inc))

(define (pi-sum a b)
  (define (pi-term x)
    (/ 1.0 (* x (+ x 2))))
  (define (pi-next x)
    (+ x 4))
  (sum pi-term a b pi-next))
