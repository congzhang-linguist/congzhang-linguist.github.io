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

<div class="repositories d-flex flex-wrap justify-content-between align-items-stretch">
  {% for repo in site.data.repositories.github_repos %}
    <div class="repo-container col-12 col-md-5 d-flex flex-column p-3 mb-4 border rounded">
      
      <div class="repo-content flex-grow-0">
        {% include repository/repo.html repository=repo.id %}
      </div>
      
      {% if repo.recommendation %}
        <div class="repo-recommendation mt-auto p-2 italic" style="border-top: 1px solid #eee; font-size: 0.9rem;">
          <strong>Note:</strong> {{ repo.recommendation }}
        </div>
      {% endif %}

    </div>
  {% endfor %}
</div>
