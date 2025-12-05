#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char *determiners[] = {"a", "the", "our", "their"};
char *nouns[] = {"boy", "girl", "pizza", "dog", "teacher", "sloth", "bannana"};
char *verbs[] = {"jumps", "runs", "eats", "sleeps", "thinks", "plays"};
char *adjectives[] = {"blue", "miniscule", "old(unc)", "smart", "tired", "massive"};
char *adverbs[] = {"quickly", "sadly", "slowly", "loudly", "happily"};
char *prepositions[] = {"near", "over", "under", "behind", "beside"};

#define DETERMINER_COUNT 4
#define NOUN_COUNT 7
#define VERB_COUNT 6    
#define ADJECTIVE_COUNT 6
#define ADVERB_COUNT 5
#define PREPOSITION_COUNT 5


char* randomDeterminer() {
    return determiners[rand() % DETERMINER_COUNT];
}

char* randomNoun() {
    return nouns[rand() % NOUN_COUNT];
}

char* randomVerb() {
    return verbs[rand() % VERB_COUNT];
}

char* randomAdjective() {
    return adjectives[rand() % ADJECTIVE_COUNT];
}

char* randomAdverb() {
    return adverbs[rand() % ADVERB_COUNT];
}

char* randomPreposition() {
    return prepositions[rand() % PREPOSITION_COUNT];
}


void simpleSentence() {
    printf("%s %s %s.\n",
        randomDeterminer(),
        randomNoun(),
        randomVerb()
    );
}


void nounPhrase(char *buffer) {
    int choice = rand() % 2;

    if (choice == 0) {

        sprintf(buffer, "%s %s",
            randomDeterminer(),
            randomNoun()
        );
    } else {
        
        sprintf(buffer, "%s %s %s",
            randomDeterminer(),
            randomAdjective(),
            randomNoun()
        );
    }
}

void prepositionalPhrase(char *buffer) {
    char noun_buffer[100];
    nounPhrase(noun_buffer);

    sprintf(buffer, "%s %s",
        randomPreposition(),
        noun_buffer
    );
}


void verbPhrase(char *buffer) {
    int choice = rand() % 2;

    if (choice == 0) {
        sprintf(buffer, "%s", randomVerb());
    } else {
        sprintf(buffer, "%s %s",
            randomVerb(),
            randomAdverb()
        );
    }
}

void complicatedSentence() {
    char noun_buf[100];
    char verb_buf[100];
    char prep_buf[100];

    nounPhrase(noun_buf);
    verbPhrase(verb_buf);
    prepositionalPhrase(prep_buf);

    printf("%s %s %s.\n", noun_buf, verb_buf, prep_buf);
}



int main() {
    srand(time(NULL));

    printf("Simple Sentence:\n");
    simpleSentence();

    printf("\nComplicated Sentence:\n");
    complicatedSentence();

    return 0;
}
