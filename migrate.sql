-- This script is for migrating the database of the old Symfony site database to Django
UPDATE django_site SET domain = 'gergely.polonkai.eu', name = 'gergely.polonkai.eu' WHERE id = 1;
INSERT INTO taggit_tag (id, name, slug) SELECT id, name, slug FROM tags;
INSERT INTO taggit_taggeditem (id, tag_id, object_id, content_type_id) SELECT tagging.id, tagging.tag_id, tagging.resource_id, django_content_type.id FROM tagging, django_content_type WHERE django_content_type.name = 'post' AND django_content_type.app_label = 'blog';
INSERT INTO blog_post (id, user_id, created_at, title, slug, content, draft) SELECT id, user_id, created_at, title, slug, content, draft FROM blog_posts;
INSERT INTO blog_codechunk (id, language, created_at, title, slug, description, content) SELECT id, language, NOW(), title, slug, description, content FROM code_chunks;
