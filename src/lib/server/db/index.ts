import { drizzle } from 'drizzle-orm/better-sqlite3';
import Database from 'better-sqlite3';
import * as schema from './schema';
import { env } from '$env/dynamic/private';
import fs from 'node:fs';
import path from 'node:path';

if (!env.DATABASE_URL) throw new Error('DATABASE_URL is not set');

const rawPath = env.DATABASE_URL || './local.db';
const cleanPath = rawPath.replace(/^file:/, '');

// Ensure the directory exists before initializing SQLite
const dir = path.dirname(cleanPath);
if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
}

const client = new Database(cleanPath);

export const db = drizzle(client, { schema });
