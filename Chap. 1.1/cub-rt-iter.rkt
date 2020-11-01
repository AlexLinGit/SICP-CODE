#lang sicp

(define (cub-rt x)
  (cub-iter 1.0 x))

(define (cub-iter guess a)
  (if (good-enough? guess a)
      guess
      (cub-iter (improve guess a) a)))

(define (improve guess a)
  (/ (+ (* 2 guess)
        (/ a (square guess)))
     3))

(define (good-enough? guess a)
  (< (abs (- guess
             (improve guess a)))
     (* (improve guess a)
        0.0000000001)))

(define (square x)
  (* x x))


  
