# Χρονοπρογραμματισμός εξετάσεων
Ο χρονοπρογραμματισμός αποτελεί σημαντικό κομμάτι σε πολλούς τομείς της καθημερινότητας.Ένας από αυτούς είναι στο κομμάτι της εκπαίδευσης στον οποίο εμφανίζεται κυρίως με δύο μορφές οι οποίες είναι το χρονοδιάγραμμα των τάξεων και το χρονοδιάγραμμα εξετάσεων. Ο χρονοπρογραμματισμός εξετάσεων είναι μια ιδιαίτερα σημαντική αλλά και ταυτόχρονα αρκετά δύσκολη διαδικασία λόγω της πολυπλοκότητας του προβλήματος προκειμένου να αποφευχθούν οι συγκρούσεις επικαλύψεις μεταξύ των μαθημάτων. Στην συγκεκριμένη έρευνα παρουσιάζεται μια επίλυση του προβλήματος χρονοπρογραμματισμού εξετάσεων σε 13 πραγματικά προβλήματα από διάφορα πανεπιστήμια και σχολεία μέσω της χρήσης αλγορίθμων χρωματισμού γράφων.

![](https://i.stack.imgur.com/NmNJV.gif)

# Εκτέλεση του προγράμματος
Προκειμένου να εκτελέσουμε το πρόγραμμα χρειάζεται να έχουμε εγκαταστημένη την γλώσσα προγραμματισμού Python και συγκεκριμένα την έκδοση 3.7.

## Εγκατάσταση της Python για windows
**1.** Κατεβάστε την Python απο **[εδώ](https://www.python.org/downloads/release/python-370/)**. Διαλέξτε ανάμεσα στις εκδόσεις 32/64 bit ανάλογα με την αριτεκτονική του υπολογιστή σας.

**2.** Εκτελέστε το αρχείο που κατεβάσατε.
Στο πρώτο παράθυρο της εγκατάστασης βεβαιωθείτε ότι έχουν επιλεγεί τα "Εγκατάσταση εκκίνησης για όλους τους χρήστες (συνιστάται)" και το "Προσθήκη Python 3.7 σε PATH" στο κάτω μέρος. Τέλος επιλέξτε το "Install now".


Για να βεβαιωθείτε ότι έγινε με επιτυχία η εγκατάσταση ανοίξτε την γραμμή εντολών και πληκρολογίστε 

```
python --version
```
Θα λάβετε ως απάντηση την έκδοση της python που έχετε εγκαταστήσει στην προκειμένη περίπτωση η απάντηση θα είναι "python 3.7".

## Εκτέλεση του προγράμματος

**1.** Κατεβάστε το τρέχων αποθετήριο από [εδώ](https://github.com/gpachoulas/91_aads_ett/archive/master.zip) όπως φαίνεται στην παρακάτω εικόνα και αποσυμπιέστε τον φάκελο.

**2.** Μπείτε στον αποσυμπιεσμένο φάκελο ανοίξτε μια γραμμή εντολών και εκτελέστε την εντολή **pip install -r requirements.txt** προκειμένου να γίνει εγκατάσταση όλων των module που χρειάζονται για την εκτέλεση του προγράμματος

**3.** Τρέξτε το αρχείο **main** με διπλό κλίκ ή μέσω φορτωσής του στο προγράμμα **Idle** το οποίο εγκαθίσταται κατα την εγκατάσταση της python

## Τρόπος Λειτουργίας
Μόλις ο χρήστης καταφέρει να εκτελέσει με επιτυχία το πρόγραμμα θα εμφανιστεί στην γραμμή εντολών το κεντρικό μένου της εφαρμογής ως εξής:

```
[1] Load data
[2] Solve problem
[3] Check predefined solution
[4] Solve all
[5] Exit
```

###### **Πληροφορίες επιλογών του μενού**
Κάθε μία απο τις επιλογές που περιέχονται στο μενού εκτελεί τις εξής λειτουργίες:

1. **Load data**
Εμφανίζει στον χρήστη τα διαθέσιμα προς φόρτωσει αρχεία προβλήμάτων. Μετά την επιτυχή ολοκλήρωση της φόρτωσης του αρχείου εμφανίζει πληροφορίες για το πρόβλημα όπως τον αριθμό φοιτητών, εγγραφών, εξετάσεων και την πυκνότητα.

2. **Solve problem**
Επιλύει το πρόβλημα που έχει επιλεγεί απο το προηγούμενο βήμα (Load data) και εμφανίζει τον αριθμό των περιόδων που χρησιμοποιήθηκαν καθώς και το κόστος λύσης. Επίσης δημιουργεί και το αρχείο λύσης το οποίο περιέχει τις εξετάσεις καθώς και την περίοδο στην οποία έχει τοποθετηθεί.

3. **Check predifined solution**
Ελέγχει την ορθότητα των λύσεων που δίνονται απο την εκφώνηση της εργασίας ως πρός τον αριθμό συγκρούσεων ο οποίος πρέπει να είναι μηδέν και ως προς τον αριθμό των εξετάσεων τις οποίες πρέπει να τις περιέχει όλες.

4. **Solve all**
Εκτελεί τις παραπάνω διαδικασίες αυτοματοποιημένα για όλα τα αρχεία προβλημάτων.

5. **Exit**
Τερματίζει την εκτέλεση του προγράμματος.


**Σημείωση**

Η σειρά με την οποία είναι τοποθετημένες οι επιλογές στο μενού επιλογών είναι αυτή που πρέπει να ακολουθήσει και ο χρήστης για την ορθή εκτέλεση του προγράμματος.

