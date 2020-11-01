#lang sicp

(define (fast-expt-iter b n a)
  (cond ((= n 1) a)
        ((even n) (fast-expt-iter b
                                  (/ n 2)
                                  (* a (square b))))
        (else (fast-expt-iter (square b)
                              (- n 1)
                              a))))

(define (fast-expt b n)
  (fast-expt-iter b n 1))
                      

(define (square x)
  (* x x))

(define (even x)
  (= (remainder x 2) 0))

