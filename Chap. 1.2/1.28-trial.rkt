#lang sicp

(define (square z)
  (* z z))



(define (rab-mill-test base exp m)
  (define (check x m)
    (define (check-then-square square)
      (if (and (not (= x 1))
               (not (= x (- m 1)))
               (= 1 square))
          0
          square))
    (check-then-square (remainder (square x) m)))
  (cond ((= exp 0) 1)
        ((even? exp)
            (check (rab-mill-test base (/ exp 2) m)
                    m))                    
        (else
            (remainder (* base
                         (rab-mill-test base (- exp 1) m))
                       m))))

(define (prime-iter n times)
  (define (try a)
    (cond ((= times 0) true)

