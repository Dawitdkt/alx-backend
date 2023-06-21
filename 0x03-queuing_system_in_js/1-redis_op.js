import { redis } from 'redis';

const redisClient = redis.createClient();

redisClient.on('error', err => console.log('Redis client not connected to the server: ', err));
redisClient.on('ready', () => console.log('Redis client connected to the server: '));
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

function setNewSchool(schoolName, value) {
    redisClient.set(schoolName, value, (error, replay) => { redis.print(`Reply: ${replay}`); });
}

function displaySchoolValue(schoolName) {
    redisClient.get(schoolName, (error, replay) => { console.log(replay); });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');