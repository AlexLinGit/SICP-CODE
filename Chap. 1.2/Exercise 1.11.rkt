#lang sicp

(define (f n)
  (cond ((< n 3) n)
        ((>= n 3) (+ (f (- n 1))
                     (* 2
                       (f (- n 2)))
                     (* 3
                        (f (- n 3)))))))


(define (f-iter n a b c)
   (if (= 3 n) (+ (* a 2)
                    (* b 1)
                    (* c 0))
                 (f-iter (- n 1)
                         (+ a b)
                         (+ (* 2 a) c)
                         (* 3 a))))              

(define (fv2 n)
  (if (< n 3)
      n
      (f-iter n 1 2 3)))
 
    