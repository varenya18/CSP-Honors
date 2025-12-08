#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define BUFFER_SIZE 100

char *determiners[]   = {"a", "the", "our", "their"};
char *nouns[]         = {"boy", "girl", "pizza", "dog", "teacher", "sloth", "banana"};
char *verbs[]         = {"jumps", "runs", "eats", "sleeps", "thinks", "plays"};
char *adjectives[]    = {"blue", "miniscule", "old", "smart", "tired", "massive"};
char *adverbs[]       = {"quickly", "sadly", "slowly", "loudly", "happily"};
char *prepositions[]  = {"near", "over", "under", "behind", "beside"};

#define DETERMINER_COUNT   4
#define NOUN_COUNT         7
#define VERB_COUNT         6
#define ADJECTIVE_COUNT    6
#define ADVERB_COUNT       5
#define PREPOSITION_COUNT  5

char* randomWord(char **array, int count) {
    return array[rand() % count];
}

void simpleSentence() {
    printf("%s %s %s.\n",
        randomWord(determiners, DETERMINER_COUNT),
        randomWord(nouns, NOUN_COUNT),
        randomWord(verbs, VERB_COUNT)
    );
}

void nounPhrase(char *buffer) {
    int choice = rand() % 2;

    if (choice == 0) {
        snprintf(buffer, BUFFER_SIZE, "%s %s",
            randomWord(determiners, DETERMINER_COUNT),
            randomWord(nouns, NOUN_COUNT)
        );
    } else {
        snprintf(buffer, BUFFER_SIZE, "%s %s %s",
            randomWord(determiners, DETERMINER_COUNT),
            randomWord(adjectives, ADJECTIVE_COUNT),
            randomWord(nouns, NOUN_COUNT)
        );
    }
}

void verbPhrase(char *buffer) {
    int choice = rand() % 2;

    if (choice == 0) {
        snprintf(buffer, BUFFER_SIZE, "%s",
            randomWord(verbs, VERB_COUNT)
        );
    } else {
        snprintf(buffer, BUFFER_SIZE, "%s %s",
            randomWord(verbs, VERB_COUNT),
            randomWord(adverbs, ADVERB_COUNT)
        );
    }
}

void prepositionalPhrase(char *buffer) {
    char noun_buf[BUFFER_SIZE];
    nounPhrase(noun_buf);

    snprintf(buffer, BUFFER_SIZE, "%s %s",
        randomWord(prepositions, PREPOSITION_COUNT),
        noun_buf
    );
}

void complicatedSentence() {
    char noun_buf[BUFFER_SIZE];
    char verb_buf[BUFFER_SIZE];
    char prep_buf[BUFFER_SIZE];

    nounPhrase(noun_buf);
    verbPhrase(verb_buf);
    prepositionalPhrase(prep_buf);

    printf("%s %s %s.\n", noun_buf, verb_buf, prep_buf);
}

int main() {
    srand((unsigned int)time(NULL));

    printf("Simple Sentence:\n");
    simpleSentence();

    printf("\nComplicated Sentence:\n");
    complicatedSentence();

    return 0;
}
