package com.mycompany.stack;

public class StackTest {

    public static void main(String[] args) {

        Stack stack = new Stack(2);
        stack.push(10);
        stack.push(20);
        stack.push(30);

        System.out.println("Cikarilan eleman: " + stack.pop());
        System.out.println("Cikarilan eleman: " + stack.pop());

    }

}
