#lang sicp

;accumulate high order procedure
(define (accumulate combiner null-value term a next b)
  (if (> a b)
      null-value
      (combiner (term a)
                (accumulate combiner
                            null-value
                            term
                           (next a)
                            next
                            b))))

;accumulate as iterative procedure
(define (accumulate-iter combiner null-value term a next b)
  (define (iter a result)
    (if (> a b)
        result
        (iter (next a) (combiner (term a)
                                 result))))
  (iter a null-value))

;sum in terms of accumulate
(define (sum term a next b)
  (define (combiner x y)
    (+ x y))
   (accumulate-iter combiner 0 term a next b))

;product in terms of accumulate
(define (product term a next b)
  (define (combiner x y)
    (* x y))
  (accumulate-iter combiner 1 term a next b))

;trial for sum procedure
(define (range-sum a b)
  (define (inc x)
    (+ x 1))
  (sum inc (- a 1) inc (- b 1)))






