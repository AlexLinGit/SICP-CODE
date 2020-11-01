#lang sicp

;definitions
(define (square x)
  (* x x))

;prime
(define (rab-mill-expmod base exp m)
  (define (check-sqr pre-sqr)
    (define (check pre-sqr sqr)
      (if (and (not (= pre-sqr 1))
               (not (= pre-sqr (- m 1)))
               (= sqr 1))
          0
          sqr))
    (check pre-sqr (remainder (square pre-sqr) m)))
  (cond ((= exp 0) 1)
        ((even? exp)
         (check-sqr (rab-mill-expmod base (/ exp 2) m)))
        (else (remainder (* base (rab-mill-expmod base
                                                 (- exp 1)
                                                 m))  m))))

(define (rab-mill-recur n)
  (define (try a)
    (define (check term)
      (and (not (= term 0))
           (= term 1)))
    (check (rab-mill-expmod a (- n 1) n)))
  (try (if (> n 4294967087)
           (+ 1 (random 4294967087))
           (+ 1 (random (- n 1))))))

(define (prime? n)
  (define (prime-iter n times)
    (cond ((< n 2) false)
          ((= times 0) true)
          ((rab-mill-recur n) (prime-iter n (- times 1)))
          (else false)))
  (prime-iter n 100))


;accumulate filter
(define (accumulate-filter filter combiner null-v term a next b)
  (if (> a b)
      null-v
      (if (filter a)
      (combiner (term a)
                 (accumulate-filter filter
                                   combiner
                                   null-v
                                   term
                                   (next a)
                                   next b))
      (combiner null-v
                 (accumulate-filter filter
                                   combiner
                                   null-v
                                   term
                                   (next a)
                                   next b)))))



;sum of squares of primes in a range
(define (sum-prime-sqrs a b)
  (define (filter x)
    (prime? x))    
  (define (combiner y z)
    (+ y z))
  (define (term x)
    (* x x))
  (define (next x)
    (+ x 1))
  (accumulate-filter filter combiner 0 term a next b))
                                  

;product positve integers less than n relative prime to n
(define (product-relative-prime n)
  (define (filter a)
    (= 1 (gcd n a)))
  (define (combiner x y)
    (* x y))
  (define (inc x)
    (+ x 1))
  (define (identity x)
    (* x 1))  
  (accumulate-filter filter combiner 1 identity 1 inc n))
