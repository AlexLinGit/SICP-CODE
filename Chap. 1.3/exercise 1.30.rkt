#lang racket

(define (sum term a next b)
  (define (iter a result)
    (if (> a b)
        result
        (iter (next a) (+ (term a) result))))
  (iter a 0))

(define (inc n)
  (+ n 1))

(define (cube n)
  (* n n n))

(define (sum-of-cubes a b)
  (sum cube a inc b))
