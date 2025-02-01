# @param {String} ransom_note
# @param {String} magazine
# @return {Boolean}
def can_construct(ransom_note, magazine)
    counter = magazine.chars.tally
    ransom_note.each_char do |c|
        return false if counter[c].nil? || counter[c] <= 0
        counter[c] -= 1
    end
    true
end