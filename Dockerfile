# Use the official PHP 8.2 with Apache image
FROM php:8.2-apache

# Set environment variables
ENV COMPOSER_ALLOW_SUPERUSER=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    unzip \
    libicu-dev \
    libpq-dev \
    libzip-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Install required PHP extensions
RUN docker-php-ext-install intl pdo pdo_mysql pdo_pgsql zip opcache

# Enable Apache mod_rewrite
RUN a2enmod rewrite

# Copy custom Apache config
COPY docker/apache.conf /etc/apache2/sites-available/000-default.conf

# Set working directory
WORKDIR /var/www/html

# Copy the application code
COPY . .

# Install Composer globally
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install dependencies and optimize autoloader, ignore platform requirements in case of dev machine differences
RUN composer install --no-dev --optimize-autoloader --no-scripts --no-progress --ignore-platform-reqs

# Re-run scripts (which cache clear & assets install)
# Setup a dummy .env file and environment variables so Symfony's dotenv component and cache clear doesn't crash during build
RUN touch .env && APP_ENV=prod DATABASE_URL="mysql://db_user:db_password@127.0.0.1:3306/db_name" composer run-script post-install-cmd

# Set appropriate permissions for the var folder inside Symfony
RUN chown -R www-data:www-data /var/www/html/var /var/www/html/public
RUN chmod -R 777 /var/www/html/var

# Expose port 80 (implicitly used by Render for Docker images exposing it)
EXPOSE 80

# Command to run Apache in the foreground
CMD ["apache2-foreground"]
