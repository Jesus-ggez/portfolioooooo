CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),

    email TEXT UNIQUE NOT NULL CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'), -- im not explain this
    password TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS user_profiles (
    user_id UUID PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,

    alias TEXT,
    name TEXT,

    username TEXT UNIQUE CHECK (username ~ '^@[A-Za-z0-9_]{3,30}$')
);

CREATE TABLE IF NOT EXISTS user_files (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),

    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,

    file_size BIGINT CHECK (file_size > 0),
    file_name TEXT NOT NULL,
    file_key TEXT NOT NULL, -- S3 key or path
    mime_type TEXT,

    UNIQUE(user_id, file_key)
);


-- idont explain this ... x2
CREATE INDEX idx_user_files_user_id ON user_files(user_id);
CREATE INDEX idx_user_files_profile_pic ON user_files(user_id) WHERE is_profile_pic = true;
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_user_profiles_username ON user_profiles(username);
