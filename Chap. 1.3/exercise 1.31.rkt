#lang sicp

;basic defs
(define (square x)
  (* x x))

(define (even? x)
  (= (remainder x 2) 0))

;recursive product procedure
(define (product a term b next)
  (if (> a b)
      1
      (* (term a)
         (product (next a) term b next))))

;iterative product procedure
(define (product-iter a term b next)
  (define (iter a result)
    (if (> a b)
        result
        (iter (next a) (* (term a) result))))
  (iter a 1))

;prodcut-iter test
(define (fact-iter n)
  (define (inc x)
    (+ x 1))
  (define (fact-iter-pre a b)
    (product-iter a inc b inc))
  (fact-iter-pre 1 (- n 1)))

;recursive factorial w/ product procedure
(define (pre-factorials a b)
  (define (inc x)
    (+ x 1))
  (product a inc b inc))

(define (factorials n)
  (pre-factorials 0 (- n 1)))

;approximating pi/4 recursively w/ product procedure
(define (pre-pi-4 a b)
  (define (inc z)
    (+ z 1))  
  (define (pi-4-term y)
    (if (even? y)
        (/ (+ y 2) (+ y 1.0))
          (/ (+ y 1.0) (+ y 2)))) 
  (product-iter a pi-4-term b inc))

(define (estimate-pi accuracy)
  (* (pre-pi-4 1 accuracy) 4))


