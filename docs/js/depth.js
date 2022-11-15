document.addEventListener("DOMContentLoaded", function() {

var chessTable = document.createElement('table');
chessTable.style.borderCollapse = 'collapse';
for (var i = 0; i < 8; i++) {
  var row = document.createElement('tr');
  for (var j = 0; j < 8; j++) {
    var cell = document.createElement('td');
    cell.style.width = '50px';
    cell.style.height = '50px';
    cell.style.border = '1px solid black';
    if ((i + j) % 2 == 0) {
      cell.style.backgroundColor = 'gray';
    } else {
      cell.style.backgroundColor = 'gray';
    }
    row.appendChild(cell);
  }
  chessTable.appendChild(row);
}
document.body.appendChild(chessTable);

document.body.style.backgroundColor = 'gray';

var chessTable = document.getElementsByTagName('table')[0];
for (var i = 0; i < chessTable.rows.length; i++) {
  for (var j = 0; j < chessTable.rows[i].cells.length; j++) {
    if ((i + j) % 2 == 0) {
      chessTable.rows[i].cells[j].style.borderColor = 'white';
    } else {
      chessTable.rows[i].cells[j].style.borderColor = 'black';
    }
  }
}

var blackColorPicker = document.createElement('input');
blackColorPicker.type = 'color';
blackColorPicker.value = '#000000';
blackColorPicker.addEventListener('change', function() {
  var chessTable = document.getElementsByTagName('table')[0];
  for (var i = 0; i < chessTable.rows.length; i++) {
    for (var j = 0; j < chessTable.rows[i].cells.length; j++) {
      if ((i + j) % 2 == 0) {
        chessTable.rows[i].cells[j].style.backgroundColor = blackColorPicker.value;
      }
    }
  }
});
document.body.appendChild(blackColorPicker);

var grayColorPicker = document.createElement('input');
grayColorPicker.type = 'color';
grayColorPicker.value = '#808080';
grayColorPicker.addEventListener('change', function() {
  var chessTable = document.getElementsByTagName('table')[0];
  for (var i = 0; i < chessTable.rows.length; i++) {
    for (var j = 0; j < chessTable.rows[i].cells.length; j++) {
      if ((i + j) % 2 == 1) {
        chessTable.rows[i].cells[j].style.backgroundColor = grayColorPicker.value;
      }
    }
  }
});
document.body.appendChild(grayColorPicker);

var chessTable = document.getElementsByTagName('table')[0];
var blackColorPicker = document.getElementsByTagName('input')[0];
var grayColorPicker = document.getElementsByTagName('input')[1];
chessTable.style.float = 'left';
blackColorPicker.style.float = 'left';
grayColorPicker.style.float = 'left';

var animateButton = document.createElement('button');
animateButton.innerHTML = 'Animate';
animateButton.addEventListener('click', function() {
  var chessTable = document.getElementsByTagName('table')[0];
  var blackColorPicker = document.getElementsByTagName('input')[0];
  var grayColorPicker = document.getElementsByTagName('input')[1];
  var animateButton = document.getElementsByTagName('button')[0];
  var intervalId = setInterval(function() {
    for (var i = 0; i < chessTable.rows.length; i++) {
      for (var j = 0; j < chessTable.rows[i].cells.length; j++) {
        if ((i + j) % 2 == 0) {
          chessTable.rows[i].cells[j].style.borderColor = 'white';
        } else {
          chessTable.rows[i].cells[j].style.borderColor = 'black';
        }
      }
    }
    setTimeout(function() {
      for (var i = 0; i < chessTable.rows.length; i++) {
        for (var j = 0; j < chessTable.rows[i].cells.length; j++) {
          if ((i + j) % 2 == 0) {
            chessTable.rows[i].cells[j].style.borderColor = 'black';
          } else {
            chessTable.rows[i].cells[j].style.borderColor = 'white';
          }
        }
      }
    }, 500);
  }, 1000);
  animateButton.addEventListener('click', function() {
    clearInterval(intervalId);
  });
});
document.body.appendChild(animateButton);

var animate2Button = document.createElement('button');
animate2Button.innerHTML = 'Animate2';
animate2Button.addEventListener('click', function() {
  var chessTable = document.getElementsByTagName('table')[0];
  var blackColorPicker = document.getElementsByTagName('input')[0];
  var grayColorPicker = document.getElementsByTagName('input')[1];
  var animate2Button = document.getElementsByTagName('button')[1];
  var intervalId = setInterval(function() {
    for (var i = 0; i < chessTable.rows.length; i++) {
      for (var j = 0; j < chessTable.rows[i].cells.length; j++) {
        if ((i + j) % 2 == 0) {
          chessTable.rows[i].cells[j].style.backgroundColor = grayColorPicker.value;
        } else {
          chessTable.rows[i].cells[j].style.backgroundColor = blackColorPicker.value;
        }
      }
    }
    setTimeout(function() {
      for (var i = 0; i < chessTable.rows.length; i++) {
        for (var j = 0; j < chessTable.rows[i].cells.length; j++) {
          if ((i + j) % 2 == 0) {
            chessTable.rows[i].cells[j].style.backgroundColor = blackColorPicker.value;
          } else {
            chessTable.rows[i].cells[j].style.backgroundColor = grayColorPicker.value;
          }
        }
      }
    }, 500);
  }, 1000);
  animate2Button.addEventListener('click', function() {
    clearInterval(intervalId);
  });
});
document.body.appendChild(animate2Button);

var animateButton = document.getElementsByTagName('button')[0];
var animate2Button = document.getElementsByTagName('button')[1];
animateButton.style.backgroundColor = '#4CAF50';
animateButton.style.border = 'none';
animateButton.style.color = 'white';
animateButton.style.padding = '15px 32px';
animateButton.style.textAlign = 'center';
animateButton.style.textDecoration = 'none';
animateButton.style.display = 'inline-block';
animateButton.style.fontSize = '16px';
animateButton.style.margin = '4px 2px';
animateButton.style.cursor = 'pointer';
animate2Button.style.backgroundColor = '#4CAF50';
animate2Button.style.border = 'none';
animate2Button.style.color = 'white';
animate2Button.style.padding = '15px 32px';
animate2Button.style.textAlign = 'center';
animate2Button.style.textDecoration = 'none';
animate2Button.style.display = 'inline-block';
animate2Button.style.fontSize = '16px';
animate2Button.style.margin = '4px 2px';
animate2Button.style.cursor = 'pointer';

var borderColorPicker1 = document.createElement('input');
borderColorPicker1.type = 'color';
borderColorPicker1.value = '#000000';
borderColorPicker1.addEventListener('change', function() {
  var chessTable = document.getElementsByTagName('table')[0];
  for (var i = 0; i < chessTable.rows.length; i++) {
    for (var j = 0; j < chessTable.rows[i].cells.length; j++) {
      if ((i + j) % 2 == 0) {
        chessTable.rows[i].cells[j].style.borderColor = borderColorPicker1.value;
      }
    }
  }
});
document.body.appendChild(borderColorPicker1);
var borderColorPicker2 = document.createElement('input');
borderColorPicker2.type = 'color';
borderColorPicker2.value = '#000000';
borderColorPicker2.addEventListener('change', function() {
  var chessTable = document.getElementsByTagName('table')[0];
  for (var i = 0; i < chessTable.rows.length; i++) {
    for (var j = 0; j < chessTable.rows[i].cells.length; j++) {
      if ((i + j) % 2 == 1) {
        chessTable.rows[i].cells[j].style.borderColor = borderColorPicker2.value;
      }
    }
  }
});
document.body.appendChild(borderColorPicker2);
var borderThicknessSlider = document.createElement('input');
borderThicknessSlider.type = 'range';
borderThicknessSlider.min = '1';
borderThicknessSlider.max = '5';
borderThicknessSlider.value = '1';
borderThicknessSlider.addEventListener('change', function() {
  var chessTable = document.getElementsByTagName('table')[0];
  for (var i = 0; i < chessTable.rows.length; i++) {
    for (var j = 0; j < chessTable.rows[i].cells.length; j++) {
      chessTable.rows[i].cells[j].style.borderWidth = borderThicknessSlider.value + 'px';
    }
  }
});
document.body.appendChild(borderThicknessSlider);


});
