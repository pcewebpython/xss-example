

rmvirtualenv xssexample
mkvirtualenv xssexample
edit requirements.txt use the following instead:
	MarkupSafe==1.1.1
pip install -r requirements.txt

Test
Browser entry in text box:
<script>
alert('Hello Losers!');
</script>
