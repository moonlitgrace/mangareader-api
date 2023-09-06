<img src="https://github.com/tokitou-san/MangaAPI/assets/114811070/235fe1d6-8120-49b1-90d9-3be30bcf25f2" width="250px" />
<p>
MangaAPI is a Python-based web scraping tool built with FastAPI that provides easy access to manga content from the MangaReader.to website. This API allows users to retrieve up-to-date information about various manga titles, chapters, and pages, enabling developers to create their own manga-related applications and services.
</p>

<h2>Api reference (V1)</h2>
<p>For more detailed documentation: <a href="https://manga-api-70c3.onrender.com/redoc">API Docs</a></p>
<p>
    <b>Note</b>: all endpoints which returns <code>list</code> has extra queries like <code>offset</code> and <code>limit</code> which helps for pagination by controls response length. eg: <code>/v1/popular/?offset=5&limit=5</code>
</p>
<table>
    <thead>
        <tr>
            <td><b>Endpoint</b></td>
            <td><b>Queries</b></td>
            <td><b>Valid queries</b></td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>/v1/popular/</code></td>
            <td>(basic queries)</td>
            <td>(basic queries)</td>
        </tr>
        <tr>
            <td><code>/v1/top-10/</code></td>
            <td>(basic queries)</td>
            <td>(basic queries)</td>
        </tr>
        <tr>
            <td><code>/v1/most-viewed/</code></td>
            <td>
                <code>chart</code>
                (basic queries)
            </td>
            <td><code>chart</code> - <code>today</code> <code>week</code> <code>month</code> eg: <code>/most-viewed/today/</code> (basic queries)</td>
        </tr>
        <tr>
            <td><code>/v1/manga/</code></td>
            <td>
                <code>slug</code>
                (basic queries)
            </td>
            <td><code>slug</code> - eg: <code>/manga/one-piece-3/</code> (basic queries)</td>
        </tr>
        <tr>
            <td><code>/v1/search/</code></td>
            <td>
                <code>keyword</code>
                <code>page</code>
                (basic queries)
            </td>
            <td>
                <code>keyword</code> - eg: <code>/search/?keyword=one piece/</code>
                <code>page</code> - eg: <code>/search/?page=5/</code>
                (basic queries)
            </td>
        </tr>
        <tr>
            <td><code>/v1/random/</code></td>
            <td>(basic queries)</td>
            <td>(basic queries)</td>
        </tr>
        <tr>
            <td><code>/v1/completed/</code></td>
            <td>
                <code>sort</code>
                <code>page</code>
                (basic queries)
            </td>
            <td><code>sort</code> - <code>default</code> <code>last-updated</code> <code>score</code> <code>name-ax</code> <code>release-date</code> <code>most-viewed</code> eg: <code>/completed/?sort=last-updated&page=2</code> (basic queries)</td>
        </tr>
    </tbody>
</table>

<h2>Features</h2>
<ul>
    <li><b>Effortless Scraping</b>: Harness the power of web scraping to extract manga data from <a href="mangareader.to">mangareader.to</a> effortlessly.</li>
    <li><b>FastAPI Framework</b>: Built using FastAPI, a modern, fast, web framework for building APIs with Python 3.10+.</li>
    <li><b>User-Friendly Endpoints</b>: Intuitive API endpoints for querying manga titles, chapters, and pages.</li>
    <li><b>Structured Data</b>: Get well-structured JSON responses that make it easy to integrate the scraped data into your applications.</li>
    <li><b>Real-time Updates</b>: Access the latest manga content by fetching data directly from MangaReader.to.</li>
    <li><b>Customizable</b>: The modular architecture allows for easy expansion and customization.</li>
    <li><b>Self-Hostable</b>: Deploy the API on your own server and enjoy full control over your manga data access.</li>
</ul>

<h2>Contribution</h2>
<p>
    Contributions to MangaAPI are welcome! If you encounter issues or want to add new features, feel free to open pull requests. <br>
    Give a ⭐️ if you find this project interesting and useful!
</p>

<h2>Disclaimer</h2>
<p>This project is developed for educational purposes and convenience in accessing manga content. Respect the website's terms of use and consider the legality of web scraping in your jurisdiction.</p>

<h2>License</h2>
<p>MangaAPI is released under the <a href="LICENSE">MIT License</a>.</p>
