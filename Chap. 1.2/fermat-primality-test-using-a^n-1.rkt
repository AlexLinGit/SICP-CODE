#lang sicp

(define (square x)
  (* x x))

(define (even? z)
  (= 0 (remainder z 2)))

(define (expmod base exp m)
  (cond ((= 0 exp) 1)
        ((even? exp)
           (remainder (square (expmod base (/ exp 2) m))
                         m))
        (else (remainder (* base (expmod base (- exp 1) m))
                         m))))

(define (fermat-test n times)
  (define (try a)
    (cond ((= times 0) true) 
          ((= 1 (expmod a (- n 1) n)) (fermat-test n (- times 1)))
          (else false)))
  (try times))

(define (prime? n)
  (cond ((< n 2) (display "try a new number"))
        (else (fermat-test n (- n 1)))))


             

                 
