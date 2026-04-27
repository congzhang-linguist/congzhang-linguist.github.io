---
layout: page
permalink: /repositories/
title: repositories
description: Edit the `_data/repositories.yml` and change the `github_users` and `github_repos` lists to include your own GitHub profile and repositories.
nav: false
nav_order: 4
---

## GitHub users

{% if site.data.repositories.github_users %}
<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for user in site.data.repositories.github_users %}
    {% include repository/repo_user.html username=user %}
  {% endfor %}
</div>
{% endif %}

---

## GitHub Repositories

<div class="repositories d-flex flex-wrap flex-md-row flex-column justify-content-between align-items-center">
  {% for repo_item in site.data.repositories.github_repos %}
    <div class="repo-container p-3 mb-4 border rounded">
      {% include repository/repo.html repository=repo_item.id %}
      
      {% if repo_item.recommendation %}
        <div class="repo-recommendation mt-2 text-muted italic">
          <i class="fa-solid fa-quote-left"></i> {{ repo_item.recommendation }}
        </div>
      {% endif %}
    </div>
  {% endfor %}
</div>
