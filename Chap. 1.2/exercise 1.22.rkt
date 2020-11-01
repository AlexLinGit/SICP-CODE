#lang sicp

(define (prime? n)
  (define (square x)
    (* x x))
  (define (divide? a b)
    (= 0 (remainder a b)))
  (define (find-divisor n test-divisor)
    (cond ((> (square test-divisor) n) n)
          ((divide? n test-divisor) test-divisor)
          (else (find-divisor n (next test-divisor)))))
  (define (smallest-divisor n)
    (find-divisor n 2))
  (= (smallest-divisor n) n))

(define (next test-divisor)
  (cond ((= test-divisor 2) 3)
        (else (+ 2 test-divisor))))

(define (timed-prime-test n)
  (start-prime-test n (runtime)))
(define (start-prime-test n start-time)
  (if (prime? n)
      (report-prime n (- (runtime) start-time))))
(define (report-prime n elapsed-time)
  (newline)
  (display n)
  (display " *** ")
  (display elapsed-time))

(define (even? n)
  (= 0 (remainder n 2)))

(define (search-for-primes t1 tn)
  (define (search-iter t tn)
    (if (<= t tn) (timed-prime-test t))
    (if (<= t tn) (search-iter (+ t 2) tn)))
  (search-iter (if (even? t1) (+ 1 t1) t1)
               (if (even? tn) (- tn 1) tn)))

 



                       