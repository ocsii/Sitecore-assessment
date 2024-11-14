public class Task3 {
    public static void main(String[] args) {

        char[][] minefield = {
                { ' ', ' ', 'X', 'X', ' ' },
                { 'X', 'X', ' ', 'X', ' ' },
                { ' ', 'X', 'X', ' ', 'X' },
                { 'X', ' ', 'X', ' ', 'X' },
                { ' ', 'X', ' ', 'X', 'X' }
        };

    }
}

class Position {
    int x, y;

    Position(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class State {
    Position totoshkaPosition;
    Position allyPosition;

    State(Position totoshkPosition, Position allyPosition) {
        this.totoshkaPosition = totoshkPosition;
        this.allyPosition = allyPosition;
    }
}