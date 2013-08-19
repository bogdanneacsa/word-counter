/*
 * Keeps helper functions for the word frequencies counter.
 * 
 * moduleauthor:: Bogdan Neacsa <neacsa_bogdan_valentin@yahoo.com>
 */
// Some helper flags in order to quickly find min and max frequencies.
FLAG_MAX = 1;
FLAG_MIN = -1;

WORD_FREQ_CLASSES = {}
WORD_FREQ_CLASSES[FLAG_MAX] = " max_freq",
WORD_FREQ_CLASSES[FLAG_MIN] = " min_freq"
/*
 * Disable the submit button and make an ajax POST request
 * in order to compute the word frequencies.
 */
function count_word_frequencies() {
	$('#text_submit_button').prop("disabled", true);
	$.ajax({
			  url : '/',
			  data : {'input_text' : $('#text_input').val()},
			  type : 'POST',
			  success : update_view
			});
}


/*
 * We're going to keep all the words from one frequency in a separate
 * container so we save space and have a nicer display.
 * 
 * param frequency_value: the value for the new frequency
 * param parent_table: a table element in which the new data will be inserted
 * param freq_flag: specifies if this is either the max or min frequency
 */
function create_frequency_container(frequency_value, parent_table, freq_flag) {
	var new_row = document.createElement('tr');
	new_row.className = 'space_under';
	var freq_data = document.createElement('td');
	freq_data.style.width = '12em';
	freq_data.style.verticalAlign = 'top';
	var freq_value = document.createElement('span');
	var span_class = "word_span";
	if (WORD_FREQ_CLASSES[freq_flag]) {
		span_class += WORD_FREQ_CLASSES[freq_flag];
	}
	freq_value.className = span_class;
	freq_value.innerHTML = "Frequency: " + frequency_value;
	freq_data.appendChild(freq_value);
	words_data = document.createElement('td');
	words_data.style.width = '75%';
	new_row.appendChild(freq_data);
	new_row.appendChild(words_data);
	parent_table.appendChild(new_row);
	return words_data;
}


/*
 * Clear the result div, then populate it with the new results.
 */
function update_view(data) {
	var word_frequencies = $.parseJSON(data);
	$("tbody").html("");
	// Use max and min frequency to somehow highligh the words with these
	// frequencies
	var max_frequency = word_frequencies[0][1];
	var min_frequency = word_frequencies[word_frequencies.length - 1][1];
	var current_frequency = null;	// The current frequency we are displaying
	var current_parent = null;		// The current <td> element to which we are appending entries
	var freq_flag = null;
 	for (var i = 0; i < word_frequencies.length; i++) {
		var entry = word_frequencies[i];
		if (entry[1] != current_frequency) {
			// We just switched from a frequency to a different one.
			current_frequency = entry[1];
			freq_flag = null; // Check if this is either min or max frequency.
			if (entry[1] == max_frequency) {
				freq_flag = FLAG_MAX;
			} else {
				if (entry[1] == min_frequency) {
					freq_flag = FLAG_MIN;
				}
			}
			current_parent = create_frequency_container(entry[1], $("tbody")[0], freq_flag);
		}
		// Create a new span for each word so we can add some styling
		var span = document.createElement('span');
		var span_class = "word_span";
		if (WORD_FREQ_CLASSES[freq_flag]) {
			span_class += WORD_FREQ_CLASSES[freq_flag];
		}
		span.className = span_class;
		span.innerHTML = entry[0] + ", ";
		// Then just append element to result div.
		current_parent.appendChild(span);
	}
	$('#text_submit_button').prop("disabled", false);
}
