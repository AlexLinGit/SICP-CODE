#lang sicp

;definitions
(define (even? y)
  (= 0 (remainder y 2)))

(define (square x)
  (* x x))

;expmod and check for nontrivial root
(define (rab-miller-test base exp m)
  (define (exp-mod-check pre-sqr)
    (define (check-4-nontriv pre-sqr sqr)
      (if (and (not (= pre-sqr 1))
               (not (= pre-sqr (- m 1)))
               (= sqr 1))
          0
          sqr))
     (check-4-nontriv pre-sqr (remainder (square pre-sqr) m)))
  ;modified expmod for check 
  (cond ((= exp 0) 1)
        ((even? exp)
            (exp-mod-check (rab-miller-test base (/ exp 2) m)))
        (else (remainder (* base
                            (rab-miller-test base (- exp 1) m))
                          m))))

;check if expmod signaled a non-triv root or if the term equals
;one and compeletes fermat's theorem
(define (rab-mill-test-recursion n)
  (define (try a)
    (define (check term)
      (and (not (= term 0)) (= term 1)))
    (check (rab-miller-test a (- n 1) n)))
  (try (if (> n 4294967087)
           (+ 1 (random 4294967087))
           (+ 1 (random (- n 1))))))
            
;iteration of the algorithm to improve probability of certainty
;of prime
(define (prime-iter n times)
  (cond ((< n 2) (display "try a number 1<n<infinity"))
        ((= times 0) true)
        ((rab-mill-test-recursion n) (prime-iter n
                                                (- times 1)))
        (else false)))

;100 is arbritary times to perform, but provides a very high
;probability of a prime number being prime
(define (prime? n)
  (prime-iter n 100))

  
