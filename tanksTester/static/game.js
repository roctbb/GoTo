var ctx, canvas;
var width = 1200;
var height = 720;
var textures = {};
var tileSize = 40;
var fetchIntervalId;

main();

window.addEventListener('load', function(){
    canvas = document.getElementById('canvas');
    canvas.width = width;
    canvas.height = height;
    ctx = canvas.getContext('2d');

    fetchIntervalId = setInterval(fetchState, 600);
    // setInterval(redraw, 2000, field);
});

function redraw(map) {
    if (width !== window.innerWidth || height !== window.innerHeight) {
        width = window.innerWidth;
        height = window.innerHeight;
        if (18.0 / 30 * width < height) {
            // fit horizontal
            canvas.height = width * 18.0 / 30;
            canvas.width = width;
        } else {
            // fit vertical
            canvas.height = height;
            canvas.width = height * 30 / 18.0;
        }
        tileSize = canvas.width / 30.0;
    }
    ctx.clearRect(0, 0, width, height);
    for (var x = 0; x < map.length; x++) {
        for (var y = 0; y < map[0].length; y++) {
            switch (map[x][y]) {
                case '#':
                    ctx.drawImage(textures.brick, x * tileSize, y * tileSize, tileSize, tileSize);
                    break;
                case '@':
                    ctx.drawImage(textures.coin, x * tileSize, y * tileSize, tileSize, tileSize);
                    if ((x > 0 && (map[x - 1][y] === '&larr;' || map[x - 1][y] === '&rarr;')) ||
                        (x < map.length - 1 && (map[x + 1][y] === '&larr;' || map[x + 1][y] === '&rarr;'))) {
                        ctx.drawImage(textures.horiz, x * tileSize, y * tileSize, tileSize, tileSize);
                    }
                    if ((y > 0 && (map[x][y - 1] === '&uarr;' || map[x][y - 1] === '&darr;')) ||
                        (y < map[0].length - 1 && (map[x][y + 1] === '&uarr;' || map[x][y + 1] === '&darr;'))) {
                        ctx.drawImage(textures.verti, x * tileSize, y * tileSize, tileSize, tileSize);
                    }
                    break;
                case '&larr;':
                case '&rarr;':
                    ctx.drawImage(textures.horiz, x * tileSize, y * tileSize, tileSize, tileSize);
                    if ((y > 0 && (map[x][y - 1] === '&uarr;' || map[x][y - 1] === '&darr;')) ||
                        (y < map[0].length - 1 && (map[x][y + 1] === '&uarr;' || map[x][y + 1] === '&darr;'))) {
                        ctx.drawImage(textures.verti, x * tileSize, y * tileSize, tileSize, tileSize);
                    }
                    break;
                case '&uarr;':
                case '&darr;':
                    ctx.drawImage(textures.verti, x * tileSize, y * tileSize, tileSize, tileSize);
                    if ((x > 0 && (map[x - 1][y] === '&larr;' || map[x - 1][y] === '&rarr;')) ||
                        (x < map.length - 1 && (map[x + 1][y] === '&larr;' || map[x + 1][y] === '&rarr;'))) {
                        ctx.drawImage(textures.horiz, x * tileSize, y * tileSize, tileSize, tileSize);
                    }
                    break;
                case '.':
                    break;
                default:
                    ctx.drawImage(textures.player, x * tileSize, y * tileSize, tileSize, tileSize);
                    ctx.fillStyle = '#ffffff';
                    var w_name = ctx.measureText(map[x][y].name).width;
                    var w_life = ctx.measureText(map[x][y].life.toString()).width;
                    ctx.fillText(map[x][y].name, (x + 0.5) * tileSize - w_name / 2, (y + 0.3) * tileSize);
                    if (map[x][y].hit === 1) ctx.fillStyle = '#ff0000';
                    ctx.fillText(map[x][y].life.toString(), (x + 0.5) * tileSize - w_life / 2,(y + 0.6) * tileSize);
                    break;
            }
        }
    }

}

function fetchState() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/state', true);
    xhr.send();
    xhr.onreadystatechange = function() {
        if (xhr.readyState !== 4) return;
        if (xhr.status === 200) {
            var map = JSON.parse(xhr.responseText);
            redraw(map);
        }
    }
}

function main() {
    var files = ["player", "grass", "brick", "coin", "horiz", "verti"];
    for (var i = 0; i < files.length; i++) {
        textures[files[i]] = new Image();
        textures[files[i]].src = '/static/res/' + files[i] + '.png';
        // textures[files[i]].src = 'res/' + files[i] + '.png';
    }
}