#lang sicp

(define (mult a b)
  (if (or (= a 0) (= b 0))
      0
      (+ a (mult a (- b 1)))))
