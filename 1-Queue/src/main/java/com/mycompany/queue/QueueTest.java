package com.mycompany.queue;

public class QueueTest {

    public static void main(String[] args) {
        Queue queue = new Queue(20);

        for (int i = 1; i <= 20; i++) {
            System.out.println("");
            queue.enqueue(i);
            queue.display();

        }

        System.out.println("Su anki eleman sayisi... " + queue.getSize());

        for (int i = 1; i <= 20; i++) {

            System.out.println("\nSiliniyor..." + queue.dequeue());
            queue.display();
        }

        System.out.println("Su anki eleman sayisi... " + queue.getSize());

    }

}
