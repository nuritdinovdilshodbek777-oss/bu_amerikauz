<!DOCTYPE html>
<html>
<head>
    <title>Бу АмерикаУЗ®</title>
</head>
<body>
    <h1>Бу АмерикаУЗ®</h1>
    <ul>
        {% for article in articles %}
            <li>
                <h2>{{ article.title }}</h2>
                <p>{{ article.content }}</p>
                <small>{{ article.published_at }}</small>
            </li>
        {% endfor %}
    </ul>
</body>
</html>