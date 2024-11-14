import java.lang.Math;
import java.util.ArrayList;

public class Task1 {
    public static void main(String[] args) {

    }
}

abstract class GeometricFigures {
    public abstract void move(double moveX, double moveY);

    public abstract void rotate(double angle);
}

class Point extends GeometricFigures {

    // Line represented by two coordinates
    private double x, y;

    // Constructor
    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }

    // Setter
    public void setCoordinates(double newX, double newY) {
        this.x = newX;
        this.y = newY;
    }

    // Getter
    public double[] getCoordinates() {
        return new double[] { this.x, this.y };
    }

    @Override
    public void move(double moveX, double moveY) {
        this.x += moveX;
        this.y += moveY;
    }

    @Override
    public void rotate(double angle) {
        // Cannot rotate a point

    }
}

class Line extends GeometricFigures {

    // Line represented by two "Points"
    private Point frontPoint, backPoint;

    // Constructor
    public Line(Point frontPoint, Point backPoint) {
        this.frontPoint = frontPoint;
        this.backPoint = backPoint;
    }

    // Setter
    public void setPoints(Point frontPoint, Point backPoint) {
        this.frontPoint = frontPoint;
        this.backPoint = backPoint;
    }

    // Getter
    public Point[] getPoints() {
        return new Point[] { frontPoint, backPoint };
    }

    // Apply movement to both points to keep length
    @Override
    public void move(double moveX, double moveY) {

        this.frontPoint.move(moveX, moveY);
        this.backPoint.move(moveX, moveY);
    }

    // Rotate line
    // Assuming it is rotated on midpoint (centre between two points)
    @Override
    public void rotate(double angle) {

        double[] frontPoints = frontPoint.getCoordinates();
        double[] backPoints = backPoint.getCoordinates();

        // Calculate Midpoint
        double midX = (frontPoints[0] + backPoints[0]) / 2;
        double midY = (frontPoints[1] + backPoints[1]) / 2;

        // Calculate new Points
        // Formula - https://academo.org/demos/rotation-about-point/
        // The formula rotates the point about the origin
        // x' = x cos 0 - y sin 0
        // y' = y cos 0 + x sin 0
        // 0 is angle in radians

        // Convert to radians
        double radianAngle = Math.toRadians(angle);

        // Move points so midpoint is origin
        double frontX = frontPoints[0] - midX;
        double frontY = frontPoints[1] - midY;
        double backX = backPoints[0] - midX;
        double backY = backPoints[1] - midY;

        // Calculate new points
        double newFrontX = (frontX * Math.cos(radianAngle)) - (frontY * Math.sin(radianAngle));
        double newFrontY = (frontY * Math.cos(radianAngle)) + (frontX * Math.sin(radianAngle));

        double newBackX = (backX * Math.cos(radianAngle)) - (backY * Math.sin(radianAngle));
        double newBackY = (backY * Math.cos(radianAngle)) + (backX * Math.sin(radianAngle));

        // Move back and update new coordinates
        frontPoint.setCoordinates((newFrontX + midX), (newFrontY + midY));
        backPoint.setCoordinates((newBackX + midX), (newBackY + midY));
    }
}

class Circle extends GeometricFigures {

    // Circle made up of "Point" and radius
    private Point centre;
    private double radius;

    // Constructor
    public Circle(Point centre, double radius) {
        this.centre = centre;
        this.radius = radius;
    }

    // Setter
    public void setCircle(Point centre, double radius) {
        this.centre = centre;
        this.radius = radius;
    }

    // Getter
    public Point getCentre() {
        return this.centre;
    }

    // Getter
    public double getRadius() {
        return this.radius;
    }

    @Override
    public void move(double moveX, double moveY) {
        this.centre.move(moveX, moveY);
    }

    @Override
    public void rotate(double angle) {
        // Rotating circle makes no difference

    }
}

class Aggregation extends GeometricFigures {

    // List contain any amount and any figure
    private ArrayList<GeometricFigures> figures;

    // Constructor
    public Aggregation() {
        this.figures = new ArrayList<>();
    }

    public void addFigure(GeometricFigures figure) {
        this.figures.add(figure);
    }

    public ArrayList<GeometricFigures> getFigures() {
        return this.figures;
    }

    @Override
    public void move(double moveX, double moveY) {
        for (GeometricFigures figure : figures) {
            figure.move(moveX, moveY);
        }
    }

    @Override
    public void rotate(double angle) {
        for (GeometricFigures figure : figures) {
            figure.rotate(angle);
        }
    }

}