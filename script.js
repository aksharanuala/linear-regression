async function predict() {

    let gre = document.getElementById("gre").value;
    let toefl = document.getElementById("toefl").value;
    let lor = document.getElementById("lor").value;
    let cgpa = document.getElementById("cgpa").value;
    let research = document.getElementById("research").value;
    if (gre === "" || toefl === "" || lor === "" || cgpa === "") {
    document.getElementById("result").innerText =
        "Please fill all the fields.";
    return;
}
    let response = await fetch(
        `http://127.0.0.1:8000/predict?gre=${gre}&toefl=${toefl}&lor=${lor}&cgpa=${cgpa}&research=${research}`
    );

    let data = await response.json();

    document.getElementById("result").innerText =
        "Chance of Admit: " + (data.chance_of_admit * 100).toFixed(2) + "%";
}