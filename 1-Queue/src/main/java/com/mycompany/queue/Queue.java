package com.mycompany.queue;

public class Queue {

    private int[] _elements;
    private int _size = 0;
    private int _capacity = 8;

    public Queue() {
        _elements = new int[_capacity];
    }

    public Queue(int capacity) {
        _capacity = capacity;
        _elements = new int[_capacity];

    }

    public boolean isEmpty() {
        return _size == 0;

    }

    public int getSize() {

        return _size;

    }

    public void enqueue(int v) {
        if (_size == _capacity) {
            System.out.println("Overflow...");
        } else {

            _elements[_size] = v;
            System.out.println("Ekleniyor..." + v);
            _size++;
        }

    }

    public int dequeue() {
        if (isEmpty()) {
            System.out.println("Underflow...");
            return -1;

        } else {
            int number = _elements[0];
            for (int i = 0; i < _size - 1; i++) {
                _elements[i] = _elements[i + 1];
            }
            _size--;
            return number;

        }

    }

    public void display() {
        System.out.print("Kuyruk elemanlari: ");
        for (int i = _size - 1; i >= 0; i--) { 
            System.out.print(_elements[i] + " -> ");
        }
        System.out.println("null"); // Kuyruğun sonunu belirtmek için
    }
}
