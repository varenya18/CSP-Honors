#include <stdio.h>
#include <stdlib.h>

// Draw lines for one quadrant
// startX, startY: starting position on axes
// xChange, yChange: how much to move each iteration
void draw_quadrant(FILE *f, int startX, int startY, int xChange, int yChange, int *hue) {
    int x = startX;
    int y = startY;

    for (int i = 0; i < 16; i++) {
        // Line from (0, y) to (x, 0)
        fprintf(f, "%d,%d,%d,%d,%d\n", 0, y, x, 0, *hue);

        // Change color 
        *hue = (*hue + 5) % 360;

        // Move to next position
        y += yChange;
        x += xChange;
    }
}

int main() {
    FILE *f = fopen("lines.csv", "w");
    if (!f) {
        perror("Failed to open file");
        return 1;
    }

    fprintf(f, "x1,y1,x2,y2,hue\n");

    int hue = 0;

    // Top-right quadrant
    draw_quadrant(f, 0, 150, 10, -10, &hue);

    // Bottom-right quadrant
    draw_quadrant(f, 150, 0, -10, -10, &hue);

    // Bottom-left quadrant
    draw_quadrant(f, 0, -150, -10, 10, &hue);

    // Top-left quadrant
    draw_quadrant(f, -150, 0, 10, 10, &hue);

    fclose(f);
    printf("Generated lines.csv with 64 lines\n");

    return 0;
}