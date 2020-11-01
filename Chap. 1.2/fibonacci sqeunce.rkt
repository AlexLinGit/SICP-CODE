#lang sicp

(define (fib n)
	(cond ((= n 0) 0)
	          ((= n 1) 1)
	          (else (+ (fib (- n 1))
		           (fib (- n 2))))))

(define theta (/ (+ 1 (sqrt 5)) 2))

(define (fibn-guess n)
  (/ (expt theta n) (sqrt 5)))

(define (fib-iter a b count)
  (if (= count 0)
      a
      (fib-iter b (+ a b) (- count 1))))

(define (fibv2 n)
  (fib-iter 0 1 n))

