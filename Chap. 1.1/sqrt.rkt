#lang sicp

(define (sqrt-iter x guess)
  (if (good-enough x guess)
      guess
      (sqrt-iter x (improve x guess))))

(define (good-enough x guess)
  (< (abs (- (improve x guess)
        guess))
     (* guess 0.00001)))

(define (improve x guess)
  (avg (/ x guess) guess))

(define (avg x y)
  (/ (+ x y) 2))

(define (sqrt x)
  (sqrt-iter x 1.0))



              