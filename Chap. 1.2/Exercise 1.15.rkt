#lang sicp

(define (cube x) (* x x x))
(define (p x) (- (* 3 x) (* 4 (cube x))))

(define (p-count-init angle counter)
   (if (not (> (abs angle) 0.1))
       counter
       (p-count-init (/ angle 3.0) (+ 1 counter))
      ))

(define (p-count angle)
  (p-count-init angle 0))

(define (sine angle)
   (if (not (> (abs angle) 0.1))
       angle
       (p (sine (/ angle 3.0)))))

