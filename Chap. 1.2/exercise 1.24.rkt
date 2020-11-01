#lang sicp
  
;Definitions                      
(define (square x)
    (* x x))

(define (divide? a b)
    (= 0 (remainder a b)))

(define (next test-divisor)
  (cond ((= test-divisor 2) 3)
        (else (+ 2 test-divisor))))

(define (even? n)
  (= 0 (remainder n 2)))


;primality test
(define (prime? n)
  (define (expmod base exp m)
    (cond ((= exp 0) 1)
          ((even? exp) (remainder (square (expmod base (/ exp 2) m))
                                  m))
          (else (remainder (* base
                              (expmod base (- base 1) (m)))
                           m))))
  (define 

 
                      
;run time
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


;search for primes in range
(define (search-for-primes t1 tn)
  (define (search-iter t tn)
    (if (<= t tn) (timed-prime-test t))
    (if (<= t tn) (search-iter (+ t 2) tn)))
  (search-iter (if (even? t1) (+ 1 t1) t1)
               (if (even? tn) (- tn 1) tn)))

