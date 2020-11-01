#lang sicp

(define (prime n)
  (= n (smallest-divisor n)))

(define (smallest-divisor n)
  (find-divisor n 2))

(define (find-divisor n test-divisor)
  (cond ((> (square test-divisor) n) n)
        ((divide? test-divisor n) test-divisor)
        (else (find-divisor n (+ 1 test-divisor)))))

(define (divide? test-divisor n)
  (= (remainder n test-divisor) 0))

(define (square n)
  (* n n))


