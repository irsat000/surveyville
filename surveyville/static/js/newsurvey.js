function newanswer(element) {
    var question = $(element).closest('.question_content');
    var count = $('.ns-right_container').find('.question_container').length;
    var answerhtml = `<div class="answer_item">
                            <span class="answer_index">Cevap: <button class="deleteanswer" onclick="deleteanswer(this)">Sil</button></span>
                            <input name="` + count + `-answer" type="text" placeholder="Cevap">
                        </div>`;
    question.append(answerhtml);
}

function deleteanswer(element) {
    var answer = $(element).closest('.answer_item');
    answer.remove();
}

function questionfade(question) {
    $(".question_container").removeClass("tab-fade");
    $(question).addClass("tab-fade");
    setTimeout(function() {
        $(".question_container").removeClass("tab-activeq");
        $(question).addClass("tab-activeq");
    }, 200);
}

function tabactivecolor(questionindex) {
    $(".question_listitem").removeClass("tab-active");
    $(questionindex).addClass("tab-active");
}

function showquestion(element) {
    var questionindex = $(element).attr("data-questionindex");
    var question = $(".ns-right_container").find("[data-question='" + questionindex + "']");
    questionfade(question);
    tabactivecolor(element);
}

function newquestion(element) {
    var count = $('.ns-right_container').find('.question_container').length;
    var questionhtml = `<div class="question_container" data-question="` + (count + 1) + `">
                            <input type="hidden" name="questionid" value="` + (count + 1) + `">
                            <span class="question_index">Soru ` + (count + 1) + `:</span>
                            <div class="question_content">
                                <input name="` + (count + 1) + `-question" type="text" placeholder="Soru">
                                <button class="addanswer" type="button" onclick="newanswer(this)">Cevap ekle</button>
                                <div class="answer_item">
                                    <span class="answer_index">Cevap: <button class="deleteanswer" type="button" onclick="deleteanswer(this)">Sil</button></span>
                                    <input name="` + (count + 1) + `-answer" type="text" placeholder="Cevap">
                                </div>
                                <div class="answer_item">
                                    <span class="answer_index">Cevap: <button class="deleteanswer" type="button" onclick="deleteanswer(this)">Sil</button></span>
                                    <input name="` + (count + 1) + `-answer" type="text" placeholder="Cevap">
                                </div>
                            </div>
                        </div>`;
    $(".ns-right_container").append(questionhtml);
    var questionindexhtml = `<div class="question_listitem" data-questionindex="` + (count + 1) + `" onclick="showquestion(this)">Soru ` + (count + 1) + `</div>`;
    $(".questionlist_wrap").append(questionindexhtml);

    var question = $(".ns-right_container").find("[data-question='" + (count + 1) + "']");
    questionfade(question);

    var questionindex = $(".questionlist_wrap").find("[data-questionindex='" + (count + 1) + "']");
    tabactivecolor(questionindex);
}

function removequestion(element) {
    $('.question_listitem').last().remove();
    $('.question_container').last().remove();

    var count = $('.ns-right_container').find('.question_container').length;
    var question = $(".ns-right_container").find("[data-question='" + count + "']");
    questionfade(question);

    var questionindex = $(".questionlist_wrap").find("[data-questionindex='" + count + "']");
    tabactivecolor(questionindex);
}