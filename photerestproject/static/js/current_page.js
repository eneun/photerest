var path = document.location.pathname;

if (path.includes("finding")) {
    result = 'Finding Friends'
} else if (path.includes("list")) {
    result = 'Feed'
} else if (path.includes("show")) {
    result = 'Feed'
} else if (path.includes('trend')) {
    result = 'Trend'
} else if (path.includes('setting')) {
    result = 'Settings'
} else if (path.includes('login')) {
    result = 'Login'
} else if (path.includes('signup')) {
    result = 'Signup'
} else if (path.includes('postcreate')) {
    result = 'New Post'
}

document.write(result)