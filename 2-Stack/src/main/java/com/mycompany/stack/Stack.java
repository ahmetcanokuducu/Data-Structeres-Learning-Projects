package com.mycompany.stack;

public class Stack {

    private int[] _elements;
    private int _size = -1;
    private int _capacity = 8;

    public Stack() {
        _elements = new int[_capacity];

    }

    public Stack(int capacity) {
        _capacity = capacity;
        _elements = new int[_capacity];
    }

    public void push(int number) {
        if (_size == _capacity - 1) {
            System.out.println("Overflow...");
        } else {

            _elements[++_size] = number;
            System.out.println(number + " eklendi...");
        }

    }

    public int pop() {
        if (_size < 0) {
            System.out.println("Underflow...");
            return -1;
        } else {
            return _elements[_size--];
        }
    }

}
